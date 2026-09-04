# Demand Experiment — Technical Schema

Формальная структура данных для Demand Validation Agent (см. Demand_Validation_Agent/README.md). Определена в Phase 12 на основе исследованного дизайна (сентябрь 2026). Это СХЕМА — конкретных экспериментов пока не проводилось (нет подключённых API/аккаунтов).

---

# Структура DemandExperiment

```
experiment_id           — уникальный ID эксперимента
product_id              — ссылка на Product ID
category                — категория товара

tier                    — cheap_backtest | professional_escalation
tier_parent_experiment_id — если tier = professional_escalation, ссылка на родительский cheap_backtest эксперимент

platform                — tiktok | instagram
test_account_id         — ссылка на запись в Account_Registry.md

creative:
  creative_id
  provider               — название сервиса генерации (Creatify/HeyGen/Replicate/fal.ai и т.д.)
  model                  — конкретная модель
  generation_mode        — image_to_video | avatar_presenter | и т.д.
  duration_seconds
  resolution
  source_assets:         — список использованных фото/видео с обязательной ссылкой на Product_Asset_Registry.md (проверка прав)

publication:
  post_id
  published_at
  status

observation:
  window_minutes
  snapshots: [ { observed_at, views, reach, likes, comments, shares, saves, view_velocity, engagement_velocity } ]

early_signal:
  score
  view_velocity_percentile
  engagement_velocity_percentile
  share_rate_percentile
  comment_rate_percentile
  acceleration_percentile
  data_quality_score

escalation:
  eligible
  triggered
  trigger                — machine-readable причина (не свободный текст)
  trigger_metrics
  triggered_at

compliance:
  ai_generated
  ai_disclosure_required
  ai_disclosure_applied
  asset_rights_verified
  platform_policy_checked

calibration:
  calibration_set_id
  tier_a_quality
  tier_a_to_tier_b_correlation
  false_negative_risk
  calibration_status      — pending | validated

result:
  status                  — pending | confirmed | weak | insufficient_data
  classification
  confidence
```

---

# Статус реализации

НЕ РЕАЛИЗОВАНО — это только схема данных для будущего использования, когда появятся:

1. Подключённые API генерации видео (Creatify/HeyGen/дешёвые альтернативы).
2. Авторизованные тестовые аккаунты в TikTok/Instagram.
3. Бюджет на платные инструменты (см. открытые вопросы в Demand_Validation_Agent/README.md).

До этого момента данная схема служит ориентиром для будущей реализации и не должна восприниматься как работающий компонент системы.