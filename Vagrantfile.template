# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu2004"
  config.ssh.insert_key = false
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.provider :virtualbox do |v|
    v.memory = 1024
    v.cpus = 1
  end

  config.vm.define "sword" do |app|
    app.vm.hostname = "sword.pen"
    app.vm.network :private_network, ip: "192.168.60.4"
  end

  config.vm.define "shield" do |app|
    app.vm.hostname = "shield.pen"
    app.vm.network :private_network, ip: "192.168.60.5"
  end

  # Ansible provisioner.
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.inventory_path = "hosts"
  end
end