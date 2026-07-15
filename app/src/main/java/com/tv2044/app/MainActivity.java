package com.tv2044.app;

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
import android.util.Log;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        
        webView = new WebView(this);
        setContentView(webView);

        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setMediaPlaybackRequiresUserGesture(false);

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());
        webView.addJavascriptInterface(new TVBridge(), "TVBridge");
        webView.loadUrl("file:///android_asset/www/index.html");
    }

    public class TVBridge {
        @JavascriptInterface
        public String scanChannels() {
            return "القناة الاولى|1|🇸🇦||MBC 1|2|🇸🇦||MBC 2|3|🇸🇦||Al Jazeera|4|🇶🇦||BBC Arabic|5|🇬🇧";
        }
    }
}