# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import PhoneNumber
from . import PostalAddress22

class CommunicationAddress9(base_types._BaseFieldType):

	__slots__ = ["_AddtlCtctInf", "_CstmrSvc", "_Email", "_Phne", "_PstlAdr", "_URLAdr"]
	@property
	def AddtlCtctInf(self):
		return self._AddtlCtctInf

	@AddtlCtctInf.setter
	def AddtlCtctInf(self, value):
		self._AddtlCtctInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlCtctInf', Max256Text, False)

	@AddtlCtctInf.deleter
	def AddtlCtctInf(self):
		del self._AddtlCtctInf
		self._AddtlCtctInf = base_types.UninitialisedField(self, 'AddtlCtctInf', Max256Text, False)

	@property
	def CstmrSvc(self):
		return self._CstmrSvc

	@CstmrSvc.setter
	def CstmrSvc(self, value):
		self._CstmrSvc = value if value is not None else base_types.UninitialisedField(self, 'CstmrSvc', PhoneNumber, False)

	@CstmrSvc.deleter
	def CstmrSvc(self):
		del self._CstmrSvc
		self._CstmrSvc = base_types.UninitialisedField(self, 'CstmrSvc', PhoneNumber, False)

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if value is not None else base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if value is not None else base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', PostalAddress22, False)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', PostalAddress22, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCtctInf', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSvc', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))