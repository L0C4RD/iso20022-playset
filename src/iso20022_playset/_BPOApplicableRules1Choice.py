# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max35Text

class BPOApplicableRules1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRulesAndVrsn", "_URBPOVrsn"]
	@property
	def OthrRulesAndVrsn(self):
		return self._OthrRulesAndVrsn

	@OthrRulesAndVrsn.setter
	def OthrRulesAndVrsn(self, value):
		self._OthrRulesAndVrsn = value if value is not None else base_types.UninitialisedField(self, 'OthrRulesAndVrsn', Max35Text, False)

	@OthrRulesAndVrsn.deleter
	def OthrRulesAndVrsn(self):
		del self._OthrRulesAndVrsn
		self._OthrRulesAndVrsn = base_types.UninitialisedField(self, 'OthrRulesAndVrsn', Max35Text, False)

	@property
	def URBPOVrsn(self):
		return self._URBPOVrsn

	@URBPOVrsn.setter
	def URBPOVrsn(self, value):
		self._URBPOVrsn = value if value is not None else base_types.UninitialisedField(self, 'URBPOVrsn', DecimalNumber, False)

	@URBPOVrsn.deleter
	def URBPOVrsn(self):
		del self._URBPOVrsn
		self._URBPOVrsn = base_types.UninitialisedField(self, 'URBPOVrsn', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRulesAndVrsn', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='URBPOVrsn', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))