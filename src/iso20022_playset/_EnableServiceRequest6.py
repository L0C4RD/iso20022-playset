from . import base_types
from .TransactionAction1Code import TransactionAction1Code
from .ActionMessage11 import ActionMessage11
from .RetailerService2Code import RetailerService2Code

class EnableServiceRequest6(base_types._BaseFieldType):

	__slots__ = ["_SvcsNbld", "_TxActn", "_DispOutpt"]
	@property
	def SvcsNbld(self):
		return self._SvcsNbld

	@SvcsNbld.setter
	def SvcsNbld(self, value):
		self._SvcsNbld = value if type(value) != base_types.auto else self.make_default("SvcsNbld")

	@SvcsNbld.deleter
	def SvcsNbld(self):
		del self._SvcsNbld
		self._SvcsNbld = None

	@property
	def TxActn(self):
		return self._TxActn

	@TxActn.setter
	def TxActn(self, value):
		self._TxActn = value if type(value) != base_types.auto else self.make_default("TxActn")

	@TxActn.deleter
	def TxActn(self):
		del self._TxActn
		self._TxActn = None

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != base_types.auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcsNbld', type=RetailerService2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxActn', type=TransactionAction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
	))

