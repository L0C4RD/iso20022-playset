# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DecimalNumber import DecimalNumber
from ._Max35Text import Max35Text

class BPOApplicableRules1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRulesAndVrsn", "_URBPOVrsn"]
	@property
	def OthrRulesAndVrsn(self):
		return self._OthrRulesAndVrsn

	@OthrRulesAndVrsn.setter
	def OthrRulesAndVrsn(self, value):
		self._OthrRulesAndVrsn = value if type(value) != base_types.auto else self.make_default("OthrRulesAndVrsn")

	@OthrRulesAndVrsn.deleter
	def OthrRulesAndVrsn(self):
		del self._OthrRulesAndVrsn
		self._OthrRulesAndVrsn = None

	@property
	def URBPOVrsn(self):
		return self._URBPOVrsn

	@URBPOVrsn.setter
	def URBPOVrsn(self, value):
		self._URBPOVrsn = value if type(value) != base_types.auto else self.make_default("URBPOVrsn")

	@URBPOVrsn.deleter
	def URBPOVrsn(self):
		del self._URBPOVrsn
		self._URBPOVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRulesAndVrsn', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='URBPOVrsn', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))