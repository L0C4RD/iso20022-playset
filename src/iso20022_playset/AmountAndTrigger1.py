import base_types
import Max35Text
import AmountOrPercentage1Choice
import Trigger1

class AmountAndTrigger1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Trggr", "_AmtDtlsChc"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Trggr(self):
		return self._Trggr

	@Trggr.setter
	def Trggr(self, value):
		self._Trggr = value if type(value) != auto else self.make_default("Trggr")

	@Trggr.deleter
	def Trggr(self):
		del self._Trggr
		self._Trggr = None

	@property
	def AmtDtlsChc(self):
		return self._AmtDtlsChc

	@AmtDtlsChc.setter
	def AmtDtlsChc(self, value):
		self._AmtDtlsChc = value if type(value) != auto else self.make_default("AmtDtlsChc")

	@AmtDtlsChc.deleter
	def AmtDtlsChc(self):
		del self._AmtDtlsChc
		self._AmtDtlsChc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trggr', type=Trigger1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtDtlsChc', type=AmountOrPercentage1Choice, min=1, max=1, mutex_group=None, array=False),
	))

