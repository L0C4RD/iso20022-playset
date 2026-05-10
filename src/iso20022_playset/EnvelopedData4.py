from . import base_types
from .Recipient4Choice import Recipient4Choice
from .Number import Number
from .EncryptedContent3 import EncryptedContent3

class EnvelopedData4(base_types._BaseFieldType):

	__slots__ = ["_Rcpt", "_NcrptdCntt", "_Vrsn"]
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
	def NcrptdCntt(self):
		return self._NcrptdCntt

	@NcrptdCntt.setter
	def NcrptdCntt(self, value):
		self._NcrptdCntt = value if type(value) != base_types.auto else self.make_default("NcrptdCntt")

	@NcrptdCntt.deleter
	def NcrptdCntt(self):
		del self._NcrptdCntt
		self._NcrptdCntt = None

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
		base_types.FieldEntry(name='Rcpt', type=Recipient4Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NcrptdCntt', type=EncryptedContent3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

