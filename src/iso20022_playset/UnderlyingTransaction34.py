from . import base_types
import PaymentTransaction155
import OriginalGroupHeader21

class UnderlyingTransaction34(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInfAndCxl", "_TxInf"]
	@property
	def OrgnlGrpInfAndCxl(self):
		return self._OrgnlGrpInfAndCxl

	@OrgnlGrpInfAndCxl.setter
	def OrgnlGrpInfAndCxl(self, value):
		self._OrgnlGrpInfAndCxl = value if type(value) != auto else self.make_default("OrgnlGrpInfAndCxl")

	@OrgnlGrpInfAndCxl.deleter
	def OrgnlGrpInfAndCxl(self):
		del self._OrgnlGrpInfAndCxl
		self._OrgnlGrpInfAndCxl = None

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if type(value) != auto else self.make_default("TxInf")

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInfAndCxl', type=OriginalGroupHeader21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInf', type=PaymentTransaction155, min=0, max=None, mutex_group=None, array=True),
	))

