from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .CardPaymentEnvironment81 import CardPaymentEnvironment81

class AcceptorDiagnosticRequest13(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_AcqrrAvlbtyReqd"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def AcqrrAvlbtyReqd(self):
		return self._AcqrrAvlbtyReqd

	@AcqrrAvlbtyReqd.setter
	def AcqrrAvlbtyReqd(self, value):
		self._AcqrrAvlbtyReqd = value if type(value) != base_types.auto else self.make_default("AcqrrAvlbtyReqd")

	@AcqrrAvlbtyReqd.deleter
	def AcqrrAvlbtyReqd(self):
		del self._AcqrrAvlbtyReqd
		self._AcqrrAvlbtyReqd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrAvlbtyReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

