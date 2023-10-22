<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" type="text/css" href="../static/styles/4-common.css">
    <link rel="stylesheet" type="text/css" href="../static/styles/3-header.css">
    <link rel="stylesheet" type="text/css" href="../static/styles/3-footer.css">
    <link rel="stylesheet" type="text/css" href="../static/styles/6-filters.css">
    <link type="text/css" rel="stylesheet" href="../static/styles/8-places.css">
    <link rel="icon" href="images/icon.png" />
    <title>HBnB</title>
  </head>
  <body>
    <header>
      <div class="logo"></div>
    </header>
    <div class="container">
      <section class="filters">
        <div class="locations">
          <h3>States</h3>
          <h4>&nbsp;</h4>
          <div class="popover">
            <ul>
              {% for state in state.values() | sort(attribute='name') %}
              <li>
                <h2>{{state.name}}</h2>
                <ul>
                  {% for city in state.cities | sort(attribute='name') %}
                  <li>{{city.name}}</li>
                  {% endfor %}
                </ul>
              </li>
              {% endfor %}
            </ul>
          </div>
        </div>
        <div class="amenities">
          <h3>Amenities</h3>
          <h4>&nbsp;</h4>
          <div class="popover">
            <ul>
              {% for amenity in amenities.values() | sort(attribute='name') %}
              <li>{{ amenity.name }}</li>
              {% endfor %}
            </ul>
          </div>
        </div>
        <button type="button">Search</button>
      </section>
      <section class="places">
	<h1>Places</h1>
	{% for place in place.values() | sort(attribute='name') %}
	<article>
	  <div class="title_box">
	    <h2>{{ place.name }}</h2>
	    <div class="price_by_night">${{ place.price_by_night }}</div>
	  </div>
	  <div class="information">
	    <div class="max_guest">{{ place.max_guest }} Guests</div>
            <div class="number_rooms">{{ place.number_rooms }} Bedroom</div>
            <div class="number_bathrooms">{{ place.number_bathrooms }} Bathroom</div>
	  </div>
	  <div class="user">
            <b>Owner:</b> {{ place.user.first_name }} {{ place.user.last_name }}
          </div>
          <div class="description">
	    {{ place.description | safe}}
          </div>
	</article>
	{% endfor %}
      </section>
    </div>
    <footer>
      <p>Holberton School</p>
    </footer>
  </body>
</html>