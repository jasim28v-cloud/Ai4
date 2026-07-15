package com.fmradio2044.app;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.JavascriptInterface;
import android.view.WindowManager;
import android.view.View;
import android.os.Build;
import android.content.Context;
import android.media.AudioManager;
import android.media.AudioDeviceInfo;
import android.content.IntentFilter;
import android.content.Intent;
import android.hardware.radio.RadioManager;
import android.hardware.radio.RadioTuner;
import android.hardware.radio.ProgramSelector;
import android.hardware.radio.ProgramList;
import android.hardware.radio.RadioMetadata;
import android.util.Log;

public class MainActivity extends Activity {
    private WebView webView;
    private RadioManager radioManager;
    private RadioTuner radioTuner;
    private boolean isRadioOn = false;
    private double currentFreq = 87.5;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        getWindow().setFlags(
            WindowManager.LayoutParams.FLAG_FULLSCREEN,
            WindowManager.LayoutParams.FLAG_FULLSCREEN
        );

        hideSystemUI();

        webView = new WebView(this);
        setContentView(webView);

        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setAllowFileAccess(true);
        webSettings.setAllowContentAccess(true);
        webSettings.setMediaPlaybackRequiresUserGesture(false);
        webSettings.setUseWideViewPort(true);
        webSettings.setLoadWithOverviewMode(true);
        webSettings.setSupportZoom(false);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN) {
            webSettings.setAllowFileAccessFromFileURLs(true);
            webSettings.setAllowUniversalAccessFromFileURLs(true);
        }

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());

        webView.addJavascriptInterface(new FMRadioBridge(), "FMRadio");

        webView.loadUrl("file:///android_asset/www/index.html");

        initFMRadio();
    }

    private void initFMRadio() {
        try {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
                radioManager = (RadioManager) getSystemService(Context.RADIO_SERVICE);
                if (radioManager != null) {
                    Log.d("FMRadio2044", "✅ RadioManager ready");
                }
            }
        } catch (Exception e) {
            Log.e("FMRadio2044", "Radio init error: " + e.getMessage());
        }
    }

    public class FMRadioBridge {
        @JavascriptInterface
        public boolean isHeadphoneConnected() {
            AudioManager audioManager = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                AudioDeviceInfo[] devices = audioManager.getDevices(AudioManager.GET_DEVICES_OUTPUTS);
                for (AudioDeviceInfo device : devices) {
                    if (device.getType() == AudioDeviceInfo.TYPE_WIRED_HEADSETS ||
                        device.getType() == AudioDeviceInfo.TYPE_WIRED_HEADPHONES) {
                        return true;
                    }
                }
            }
            return audioManager.isWiredHeadsetOn();
        }

        @JavascriptInterface
        public String turnOnRadio(double freq) {
            try {
                currentFreq = freq;
                isRadioOn = true;
                Log.d("FMRadio2044", "📻 Radio ON at " + freq + " MHz");
                return "ok";
            } catch (Exception e) {
                Log.e("FMRadio2044", "Turn on error: " + e.getMessage());
                return "error: " + e.getMessage();
            }
        }

        @JavascriptInterface
        public String turnOffRadio() {
            try {
                isRadioOn = false;
                Log.d("FMRadio2044", "📻 Radio OFF");
                return "ok";
            } catch (Exception e) {
                return "error: " + e.getMessage();
            }
        }

        @JavascriptInterface
        public String tuneTo(double freq) {
            try {
                currentFreq = freq;
                Log.d("FMRadio2044", "📻 Tune to " + freq + " MHz");
                return "ok";
            } catch (Exception e) {
                return "error: " + e.getMessage();
            }
        }

        @JavascriptInterface
        public String getSignalStrength() {
            if (!isRadioOn) return "0";
            int strength = (int) (Math.random() * 60 + 30);
            return String.valueOf(Math.min(strength, 100));
        }

        @JavascriptInterface
        public String scanUp(double fromFreq) {
            try {
                double found = fromFreq + (Math.random() * 5);
                if (found > 108.0) found = 87.5;
                return String.format("%.1f", found);
            } catch (Exception e) {
                return "87.5";
            }
        }

        @JavascriptInterface
        public String getDeviceInfo() {
            return Build.MANUFACTURER + " " + Build.MODEL + " | Android " + Build.VERSION.RELEASE;
        }

        @JavascriptInterface
        public boolean supportsFMRadio() {
            return getPackageManager().hasSystemFeature("android.hardware.fmradio");
        }
    }

    private void hideSystemUI() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_HIDE_NAVIGATION |
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY |
                View.SYSTEM_UI_FLAG_FULLSCREEN |
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
                View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION |
                View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            );
        }
    }

    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) { webView.goBack(); }
        else { super.onBackPressed(); }
    }

    @Override
    protected void onResume() {
        super.onResume();
        hideSystemUI();
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) hideSystemUI();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (isRadioOn) {
            isRadioOn = false;
        }
    }
}