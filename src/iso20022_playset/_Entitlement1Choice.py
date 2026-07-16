# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max35Text

class Entitlement1Choice(base_types._BaseFieldType):

	__slots__ = ["_EntitlmntDesc", "_EntitlmntRatio"]
	@property
	def EntitlmntDesc(self):
		return self._EntitlmntDesc

	@EntitlmntDesc.setter
	def EntitlmntDesc(self, value):
		self._EntitlmntDesc = value if value is not None else base_types.UninitialisedField(self, 'EntitlmntDesc', Max35Text, False)

	@EntitlmntDesc.deleter
	def EntitlmntDesc(self):
		del self._EntitlmntDesc
		self._EntitlmntDesc = base_types.UninitialisedField(self, 'EntitlmntDesc', Max35Text, False)

	@property
	def EntitlmntRatio(self):
		return self._EntitlmntRatio

	@EntitlmntRatio.setter
	def EntitlmntRatio(self, value):
		self._EntitlmntRatio = value if value is not None else base_types.UninitialisedField(self, 'EntitlmntRatio', DecimalNumber, False)

	@EntitlmntRatio.deleter
	def EntitlmntRatio(self):
		del self._EntitlmntRatio
		self._EntitlmntRatio = base_types.UninitialisedField(self, 'EntitlmntRatio', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EntitlmntDesc', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EntitlmntRatio', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))