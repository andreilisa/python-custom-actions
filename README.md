***Custom Action for DevOps Community Day(CI/CD)***

This action do an api call to [Weather API](https://openweathermap.org/api)

**Configuration:**

```
inputs:
  open_weather_key:
    description: 'Open Weather API Key'
    required: true
  city_name:
    description: 'City Name'
    required: false
    default: 'Paris'
outputs: // console output
  weather:
    description: 'Whether'
```

**Example of using this actions:**

```
  weather:
    runs-on: ubuntu-22.04
    steps:
      - name: Weather Call
        uses: andreilisa/python-custom-actions@v1.0
        with:
          city_name: ${{ vars.CITY_NAME }}
          open_weather_key: ${{ secrets.OPEN_WEATHER_KEY }}
```

