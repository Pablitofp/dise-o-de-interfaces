package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class CatalogActivity extends AppCompatActivity {
    private Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);
        Button button = findViewById(R.id.Button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Toast.makeText(context, "Arrancando otra actividad...", Toast.LENGTH_LONG).show(); //Comprobación de que el botón funciona
                Intent myIntent = new Intent(context, DetailActivity.class);
                context.startActivity(myIntent);
            }
        });
    }
}