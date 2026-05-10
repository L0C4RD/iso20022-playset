from . import base_types
from ._AlgorithmIdentification15 import AlgorithmIdentification15
from ._Max140Binary import Max140Binary
from ._Recipient4Choice import Recipient4Choice
from ._EncapsulatedContent3 import EncapsulatedContent3
from ._Number import Number

class AuthenticatedData4(base_types._BaseFieldType):

	__slots__ = ["_NcpsltdCntt", "_MACAlgo", "_Vrsn", "_MAC", "_Rcpt"]
	@property
	def MAC(self):
		return self._MAC

	@MAC.setter
	def MAC(self, value):
		self._MAC = value if type(value) != base_types.auto else self.make_default("MAC")

	@MAC.deleter
	def MAC(self):
		del self._MAC
		self._MAC = None

	@property
	def MACAlgo(self):
		return self._MACAlgo

	@MACAlgo.setter
	def MACAlgo(self, value):
		self._MACAlgo = value if type(value) != base_types.auto else self.make_default("MACAlgo")

	@MACAlgo.deleter
	def MACAlgo(self):
		del self._MACAlgo
		self._MACAlgo = None

	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if type(value) != base_types.auto else self.make_default("NcpsltdCntt")

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MAC', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MACAlgo', type=AlgorithmIdentification15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=Recipient4Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

