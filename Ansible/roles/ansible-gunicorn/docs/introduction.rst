Introduction
============

The `Green Unicorn <http://gunicorn.org/>`_ is a Python WSGI HTTP Server for
UNIX. It uses a pre-fork worker model ported from Ruby's Unicorn project. The
Gunicorn server is broadly compatible with various web frameworks, simply
implemented, light on server resources, and fairly speedy.

The ``debops.gunicorn`` Ansible role uses the `Debian package configuration structure <https://chris-lamb.co.uk/posts/sysadmin-friendly-deployment-gunicorn-debian>`_
to manage multiple ``gunicorn`` applications as a signle service. This can be
used to deploy applications that use either a system Python installation, or
a ``virtualenv`` Python environment.


Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v2.0.0``. To install it, run:

.. code-block:: console

   ansible-galaxy install debops.gunicorn

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
