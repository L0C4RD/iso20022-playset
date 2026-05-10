from . import base_types
import PaymentRole1Choice
import CommunicationAddress10
import Max35Text

class ContactIdentificationAndAddress2(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Role", "_ComAdr"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	@property
	def ComAdr(self):
		return self._ComAdr

	@ComAdr.setter
	def ComAdr(self, value):
		self._ComAdr = value if type(value) != auto else self.make_default("ComAdr")

	@ComAdr.deleter
	def ComAdr(self):
		del self._ComAdr
		self._ComAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PaymentRole1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComAdr', type=CommunicationAddress10, min=1, max=1, mutex_group=None, array=False),
	))

