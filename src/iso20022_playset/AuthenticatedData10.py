from . import base_types
import Recipient15Choice
import Number
import AlgorithmIdentification31
import Max140Binary
import EncapsulatedContent3

class AuthenticatedData10(base_types._BaseFieldType):

	__slots__ = ["_Rcpt", "_MACAlgo", "_Vrsn", "_NcpsltdCntt", "_MAC"]
	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def MACAlgo(self):
		return self._MACAlgo

	@MACAlgo.setter
	def MACAlgo(self, value):
		self._MACAlgo = value if type(value) != auto else self.make_default("MACAlgo")

	@MACAlgo.deleter
	def MACAlgo(self):
		del self._MACAlgo
		self._MACAlgo = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if type(value) != auto else self.make_default("NcpsltdCntt")

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = None

	@property
	def MAC(self):
		return self._MAC

	@MAC.setter
	def MAC(self, value):
		self._MAC = value if type(value) != auto else self.make_default("MAC")

	@MAC.deleter
	def MAC(self):
		del self._MAC
		self._MAC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcpt', type=Recipient15Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MACAlgo', type=AlgorithmIdentification31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MAC', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
	))

