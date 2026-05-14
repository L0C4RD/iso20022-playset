# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalInformation15 import AdditionalInformation15
from ._ISODate import ISODate
from ._IndividualCostOrCharge2 import IndividualCostOrCharge2

class CostsAndCharges2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ExAnteRefDt", "_IndvCostOrChrg"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ExAnteRefDt(self):
		return self._ExAnteRefDt

	@ExAnteRefDt.setter
	def ExAnteRefDt(self, value):
		self._ExAnteRefDt = value if type(value) != base_types.auto else self.make_default("ExAnteRefDt")

	@ExAnteRefDt.deleter
	def ExAnteRefDt(self):
		del self._ExAnteRefDt
		self._ExAnteRefDt = None

	@property
	def IndvCostOrChrg(self):
		return self._IndvCostOrChrg

	@IndvCostOrChrg.setter
	def IndvCostOrChrg(self, value):
		self._IndvCostOrChrg = value if type(value) != base_types.auto else self.make_default("IndvCostOrChrg")

	@IndvCostOrChrg.deleter
	def IndvCostOrChrg(self):
		del self._IndvCostOrChrg
		self._IndvCostOrChrg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExAnteRefDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvCostOrChrg', type=IndividualCostOrCharge2, min=1, max=None, mutex_group=None, array=True),
	))