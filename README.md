Graphite importer
=================
This repository contains a Graphite importer for Pingdom monitoring metrics.

Requirements
------------
- Pingdom credentials including username, password and app-key
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
    <td>sample.example.com/td>
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

Pingdom Checks
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

Usage
-----
1. Clone the GitHub repository and change directory
2. Copy `config.yml.sample` to `config.yml`
3. Change the Pingdom credentails and Graphtie prameters in `config.yml`
4. Configure your Pingdom checks (id, name, limit)
5. Run `pingdom.py` or set up a scheduled task
