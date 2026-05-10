import base_types
import ISODate
import IndividualCostOrCharge2
import AdditionalInformation15

class CostsAndCharges2(base_types._BaseFieldType):

	__slots__ = ["_ExAnteRefDt", "_IndvCostOrChrg", "_AddtlInf"]
	@property
	def ExAnteRefDt(self):
		return self._ExAnteRefDt

	@ExAnteRefDt.setter
	def ExAnteRefDt(self, value):
		self._ExAnteRefDt = value if type(value) != auto else self.make_default("ExAnteRefDt")

	@ExAnteRefDt.deleter
	def ExAnteRefDt(self):
		del self._ExAnteRefDt
		self._ExAnteRefDt = None

	@property
	def IndvCostOrChrg(self):
		return self._IndvCostOrChrg

	@IndvCostOrChrg.setter
	def IndvCostOrChrg(self, value):
		self._IndvCostOrChrg = value if type(value) != auto else self.make_default("IndvCostOrChrg")

	@IndvCostOrChrg.deleter
	def IndvCostOrChrg(self):
		del self._IndvCostOrChrg
		self._IndvCostOrChrg = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExAnteRefDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvCostOrChrg', type=IndividualCostOrCharge2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
	))

