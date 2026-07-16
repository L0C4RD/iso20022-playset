# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate

class EligibilityDates1(base_types._BaseFieldType):

	__slots__ = ["_EntitlmntFxgDt"]
	@property
	def EntitlmntFxgDt(self):
		return self._EntitlmntFxgDt

	@EntitlmntFxgDt.setter
	def EntitlmntFxgDt(self, value):
		self._EntitlmntFxgDt = value if value is not None else base_types.UninitialisedField(self, 'EntitlmntFxgDt', ISODate, False)

	@EntitlmntFxgDt.deleter
	def EntitlmntFxgDt(self):
		del self._EntitlmntFxgDt
		self._EntitlmntFxgDt = base_types.UninitialisedField(self, 'EntitlmntFxgDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EntitlmntFxgDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))