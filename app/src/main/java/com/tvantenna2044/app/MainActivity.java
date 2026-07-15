package com.tvantenna2044.app;

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
import android.util.Log;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends Activity {
    private WebView webView;
    private boolean isTVOn = false;
    private int currentChannel = 0;

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

        webView.addJavascriptInterface(new TVAntennaBridge(), "TVAntenna");

        webView.loadUrl("file:///android_asset/www/index.html");
    }

    public class TVAntennaBridge {
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
        public String turnOnTV() {
            try {
                isTVOn = true;
                Log.d("TVAntenna2044", "📺 TV ON");
                return "ok";
            } catch (Exception e) {
                return "error: " + e.getMessage();
            }
        }

        @JavascriptInterface
        public String turnOffTV() {
            try {
                isTVOn = false;
                Log.d("TVAntenna2044", "📺 TV OFF");
                return "ok";
            } catch (Exception e) {
                return "error: " + e.getMessage();
            }
        }

        @JavascriptInterface
        public String scanChannels() {
            try {
                List<String> channels = new ArrayList<>();
                channels.add("القناة الأولى|🇸🇦|1");
                channels.add("القناة الثانية|🇸🇦|2");
                channels.add("MBC 1|🇸🇦|3");
                channels.add("MBC 2|🇸🇦|4");
                channels.add("MBC 3|🇸🇦|5");
                channels.add("MBC 4|🇸🇦|6");
                channels.add("MBC Action|🇸🇦|7");
                channels.add("MBC Max|🇸🇦|8");
                channels.add("Al Jazeera|🇶🇦|9");
                channels.add("BBC Arabic|🇬🇧|10");
                channels.add("CN Arabia|🇸🇦|11");
                channels.add("Rotana Cinema|🇸🇦|12");
                channels.add("Rotana Music|🇸🇦|13");
                channels.add("Rotana Khalijia|🇸🇦|14");
                channels.add("Spacetoon|🇸🇦|15");
                channels.add("Cartoon Network|🇺🇸|16");
                channels.add("National Geographic|🇺🇸|17");
                channels.add("Discovery Channel|🇺🇸|18");
                channels.add("FOX Movies|🇺🇸|19");
                channels.add("OSN Movies|🇸🇦|20");

                StringBuilder result = new StringBuilder();
                for (String ch : channels) {
                    result.append(ch).append("|||");
                }
                return result.toString();
            } catch (Exception e) {
                return "error: " + e.getMessage();
            }
        }

        @JavascriptInterface
        public String getSignalStrength() {
            if (!isTVOn) return "0";
            int strength = (int) (Math.random() * 50 + 40);
            return String.valueOf(Math.min(strength, 100));
        }

        @JavascriptInterface
        public String getDeviceInfo() {
            return Build.MANUFACTURER + " " + Build.MODEL + " | Android " + Build.VERSION.RELEASE;
        }

        @JavascriptInterface
        public boolean supportsTVTuner() {
            return getPackageManager().hasSystemFeature("android.hardware.tv.tuner");
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
        isTVOn = false;
    }
}