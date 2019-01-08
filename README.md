# IC3Net Environments

This repository contains gym environments for tasks used in paper for IC3Net except starcraft. Namely, this repository contains:

- Traffic Junction Environment
- Predator Prey Environments
- Sanity check number pairs and levers environment will be added later.

## Cite

Please cite IC3Net paper, "Learning when to Communicate at Scale in Multiagent Cooperative and Competitive Tasks" (ICLR 2019 accepted) if you use these environments in your work:

```
@article{singh2018learning,
  title={Learning when to Communicate at Scale in Multiagent Cooperative and Competitive Tasks},
  author={Singh, Amanpreet and Jain, Tushar and Sukhbaatar, Sainbayar},
  journal={arXiv preprint arXiv:1812.09755},
  year={2018}
}
```

## Related

- IC3Net code is available at [IC3Net/IC3Net](https://github.com/IC3Net/IC3Net)
- `gym-starcraft` is available at [apsdehal/gym-starcraft](https://github.com/apsdehal/gym-starcraft)

## Running

Run `python setup.py develop` in the locally cloned repository.
Next, run `python example/random_agent.py` for a random agent playing with Traffic Junction environment.

Note that, you can use `--display` flag to see the actual environment being rendered on console. You might not see anything as it is action and execution are very fast in case of a random agent.

## License

Code for this project is available under MIT license.

## Authors

- Amanpreet Singh ([@apsdehal](https://github.com/apsdehal))
- Tushar Jain ([@tshrjn](https://github.com/tshrjn))
