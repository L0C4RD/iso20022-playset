from . import base_types
from ._Number import Number
from ._AbnormalValuesData4 import AbnormalValuesData4

class DetailedTransactionStatistics28(base_types._BaseFieldType):

	__slots__ = ["_NbOfDerivsRptdWthOtlrs", "_Wrnngs", "_NbOfDerivsRptd"]
	@property
	def NbOfDerivsRptd(self):
		return self._NbOfDerivsRptd

	@NbOfDerivsRptd.setter
	def NbOfDerivsRptd(self, value):
		self._NbOfDerivsRptd = value if type(value) != base_types.auto else self.make_default("NbOfDerivsRptd")

	@NbOfDerivsRptd.deleter
	def NbOfDerivsRptd(self):
		del self._NbOfDerivsRptd
		self._NbOfDerivsRptd = None

	@property
	def NbOfDerivsRptdWthOtlrs(self):
		return self._NbOfDerivsRptdWthOtlrs

	@NbOfDerivsRptdWthOtlrs.setter
	def NbOfDerivsRptdWthOtlrs(self, value):
		self._NbOfDerivsRptdWthOtlrs = value if type(value) != base_types.auto else self.make_default("NbOfDerivsRptdWthOtlrs")

	@NbOfDerivsRptdWthOtlrs.deleter
	def NbOfDerivsRptdWthOtlrs(self):
		del self._NbOfDerivsRptdWthOtlrs
		self._NbOfDerivsRptdWthOtlrs = None

	@property
	def Wrnngs(self):
		return self._Wrnngs

	@Wrnngs.setter
	def Wrnngs(self, value):
		self._Wrnngs = value if type(value) != base_types.auto else self.make_default("Wrnngs")

	@Wrnngs.deleter
	def Wrnngs(self):
		del self._Wrnngs
		self._Wrnngs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfDerivsRptd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDerivsRptdWthOtlrs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wrnngs', type=AbnormalValuesData4, min=1, max=None, mutex_group=None, array=True),
	))

