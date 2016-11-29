Graphite importer
=================
This repository contains a Graphite importer for Cloudflare and Pingdom metrics.

Requirements
------------
- Pingdom credentials including username, password and app-key
- Cloudflare credentials including email address and api-key
- Graphite server as target for the importer
- Valid `config.yml` based on `config.yml.sample` in the current working directory

Parameters
----------
The following list contains all parameters that need to be set in the `carbon` section.

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Sample</th>
  </tr>
  <tr>
    <td>server</td>
    <td>Graphite server</td>
    <td>sample.example.com</td>
  </tr>
  <tr>
    <td>port</td>
    <td>Listen port on the Graphite server</td>
    <td>2003</td>
  </tr>
</table>

The following list contains all parameters that need to be set in the `pingdom` section.

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Sample</th>
  </tr>
  <tr>
    <td>username</td>
    <td>Username of your Pingdom account</td>
    <td>john@example.com</td>
  </tr>
  <tr>
    <td>password</td>
    <td>Password of your Pingdom account</td>
    <td>mysecretpassword</td>
  </tr>
  <tr>
    <td>app_key</td>
    <td>App-key that you set in the Pingdom backend</td>
    <td>mysecretappkey</td>
  </tr>
</table>

The following list contains all parameters that need to be set on the `cloudflare` section.

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Sample</th>
  </tr>
  <tr>
    <td>name</td>
    <td>Name of the Cloudflare zone</td>
    <td>example.com</td>
  </tr>
  <tr>
    <td>email</td>
    <td>E-mail address of your Cloudflare account</td>
    <td>cloudflare@example.com</td>
  </tr>
  <tr>
    <td>key</td>
    <td>Cloudflare API key</td>
    <td>a94a8fe5ccb19ba61c4c0873d391e987982fbbd3</td>
  </tr>
  <tr>
    <td>url</td>
    <td>URL to Cloudflare analyticts dashboard</td>
    <td>https://api.cloudflare.com/client/v4/zones/...</td>
  </tr>

Pingdom checks
--------------
The `pingdom_check` section in the `config.yml` is an array of dictonaries, where each dictonary represents one Pingdom check. The following list contains all parameters that need to be set for a Pingdom check.

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Sample</th>
  </tr>
  <tr>
    <td>id</td>
    <td>Pingdom check id</td>
    <td>1234567</td>
  </tr>
  <tr>
    <td>name</td>
    <td>Full path on the Graphite server</td>
    <td>www.example.com.http</td>
  </tr>
  <tr>
    <td>limit</td>
    <td>The amount of metrics to pull from Pingdom</td>
    <td>10</td>
  </tr>
</table>

Cloudflare checks
-----------------
There is no need to specify any checks for the Cloudflare importer. All metrics from the requests-, bandwidth- and threats-section will be gathered. However you can create multiple lists in the `cloudflare` section if you have more than one zone.

Usage
-----
1. Clone the GitHub repository and change directory
2. Copy `config.yml.sample` to `config.yml`
3. Change the Pingdom credentails and Graphtie prameters in `config.yml`
4. Configure your Pingdom checks (id, name, limit)
5. Run `pingdom.py` or set up a scheduled task
