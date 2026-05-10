from . import base_types
import PostalAddress22
import Max256Text
import PhoneNumber

class CommunicationAddress9(base_types._BaseFieldType):

	__slots__ = ["_AddtlCtctInf", "_Email", "_Phne", "_PstlAdr", "_CstmrSvc", "_URLAdr"]
	@property
	def AddtlCtctInf(self):
		return self._AddtlCtctInf

	@AddtlCtctInf.setter
	def AddtlCtctInf(self, value):
		self._AddtlCtctInf = value if type(value) != auto else self.make_default("AddtlCtctInf")

	@AddtlCtctInf.deleter
	def AddtlCtctInf(self):
		del self._AddtlCtctInf
		self._AddtlCtctInf = None

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if type(value) != auto else self.make_default("Email")

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = None

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if type(value) != auto else self.make_default("Phne")

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	@property
	def CstmrSvc(self):
		return self._CstmrSvc

	@CstmrSvc.setter
	def CstmrSvc(self, value):
		self._CstmrSvc = value if type(value) != auto else self.make_default("CstmrSvc")

	@CstmrSvc.deleter
	def CstmrSvc(self):
		del self._CstmrSvc
		self._CstmrSvc = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCtctInf', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSvc', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

