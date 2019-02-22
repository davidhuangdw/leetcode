require 'erb'
require 'yaml'

module YamlErbLoader
  extend self

  def load_yml(file_path, options={})
    deep_symbolize_keys load_raw_yml(file_path)
  end

  def load_raw_yml(file_path)
    # file_path += '.yml' unless file_path =~ /\.(yml|yaml)$/
    YAML.load(ERB.new(File.read(file_path)).result)
  end

  private

  def deep_symbolize_keys(hash_or_value)
      hash_or_value.is_a?(Hash) ? Hash[*hash_or_value.map{|k, v| [k.to_sym, deep_symbolize_keys(v)]}.reduce([], :+)] : hash_or_value
  end
end

