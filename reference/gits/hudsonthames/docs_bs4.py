import requests
from bs4 import BeautifulSoup
import html2text
import os
import time
import random
from requests.exceptions import RequestException

def convert_url_to_markdown(slug, max_retries=3):
    attempt = 0
    while attempt < max_retries:
        try:
            delay = random.uniform(2, 5)
            time.sleep(delay)
            
            base_url = 'https://www.mlfinlab.com/en/latest/'
            url = f'{base_url}{slug}.html'
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the specific div
            content_div = soup.find('div', {'itemprop': 'articleBody'})
            if not content_div:
                raise Exception(f"Could not find content div with id '{slug.split('/')[-1].replace('_', '-')}'")
            
            converter = html2text.HTML2Text()
            converter.ignore_links = False
            markdown_content = converter.handle(str(content_div))
            
            output_filename = f"output/{slug.replace('/', '-')}.md"
            os.makedirs('output', exist_ok=True)
            
            with open(output_filename, 'w') as md_file:
                md_file.write(markdown_content)
            
            print(f"Successfully processed {url} (delay: {delay:.2f}s)")
            return output_filename

        except (RequestException, Exception) as e:
            attempt += 1
            if attempt < max_retries:
                retry_delay = random.uniform(5, 10)
                print(f"Attempt {attempt} failed for {slug}. Error: {str(e)}. Retrying in {retry_delay:.2f}s...")
                time.sleep(retry_delay)
            else:
                print(f"Failed to process {slug} after {max_retries} attempts. Error: {str(e)}")
                return None

if __name__ == '__main__':

    # Example usage
    slugs = [
        # 'regression/history_weighted_regression',
        # 'clustering/feature_clusters',
        
        # 'backtest_overfitting/backtest_statistics',

        'data_structures/data_prep',
        'data_structures/standard',
        'data_structures/imbalance',
        'data_structures/runbars',
        'data_structures/futures_roll',
        'labeling/introduction',
        'labeling/labeling_raw_return',
        'labeling/labeling_fixed_time_horizon',
        'labeling/labeling_excess_mean',
        'labeling/labeling_excess_median',
        'labeling/labeling_vs_benchmark',
        'labeling/labeling_bull_bear',
        'labeling/labeling_matrix_flags',
        'labeling/labeling_tail_sets',
        'labeling/labeling_trend_scanning',
        'labeling/tb_meta_labeling',
        'sampling/intro_sampling',
        'sampling/sample_uniqueness',
        'sampling/sequential_boot',
        'sampling/sample_weights',
        'feature_engineering/frac_diff',
        'feature_engineering/structural_breaks',
        'feature_engineering/filters',
        'feature_engineering/volatility_estimators',
        'feature_engineering/noise_reduction',
        'feature_engineering/directional_change',
        'feature_engineering/micro_features_first_gen',
        'feature_engineering/entropy',
        'feature_engineering/micro_features_other',
        'modelling/sb_bagging',
        'clustering/onc',
        'clustering/hierarchical_clustering',
        'cross_validation/purged_embargo',
        'cross_validation/cpcv',
        'feature_importance/afm',
        'feature_importance/clustered',
        'feature_importance/fingerprint',
        'feature_importance/pca',
        'feature_importance/shapley',
        'bet_sizing/bet_sizing',
        'bet_sizing/EF3M',
        'data_generation/introduction',
        'data_generation/corrgan',
        'data_generation/vine_methods',
        'data_generation/correlated_random_walks',
        'data_generation/hcbm',
        'data_generation/bootstrap',
        'data_generation/data_verification',
        'networks/introduction',
        'networks/mst',
        'networks/almst',
        'networks/pmfg',
        'networks/visualisations',
        'networks/dash',
        'codependence/introduction',
        'codependence/correlation_based_metrics',
        'codependence/information_theory_metrics',
        'codependence/codependence_marti',
        'codependence/optimal_transport',
        'codependence/codependence_matrix',
    ]

    for slug in slugs:
        output_file = convert_url_to_markdown(slug)
        print(f"Converted {slug} to {output_file}")