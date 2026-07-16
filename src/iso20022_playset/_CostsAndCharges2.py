# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import ISODate
from . import IndividualCostOrCharge2

class CostsAndCharges2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ExAnteRefDt", "_IndvCostOrChrg"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@property
	def ExAnteRefDt(self):
		return self._ExAnteRefDt

	@ExAnteRefDt.setter
	def ExAnteRefDt(self, value):
		self._ExAnteRefDt = value if value is not None else base_types.UninitialisedField(self, 'ExAnteRefDt', ISODate, False)

	@ExAnteRefDt.deleter
	def ExAnteRefDt(self):
		del self._ExAnteRefDt
		self._ExAnteRefDt = base_types.UninitialisedField(self, 'ExAnteRefDt', ISODate, False)

	@property
	def IndvCostOrChrg(self):
		return self._IndvCostOrChrg

	@IndvCostOrChrg.setter
	def IndvCostOrChrg(self, value):
		self._IndvCostOrChrg = value if value is not None else base_types.UninitialisedField(self, 'IndvCostOrChrg', IndividualCostOrCharge2, True)

	@IndvCostOrChrg.deleter
	def IndvCostOrChrg(self):
		del self._IndvCostOrChrg
		self._IndvCostOrChrg = base_types.UninitialisedField(self, 'IndvCostOrChrg', IndividualCostOrCharge2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExAnteRefDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvCostOrChrg', type=IndividualCostOrCharge2, min=1, max=None, mutex_group=None, array=True),
	))