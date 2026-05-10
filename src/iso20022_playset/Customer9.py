from . import base_types
import ContactPersonal1
import Max2NumericText
import Address2
import Credentials3
import Max70Text

class Customer9(base_types._BaseFieldType):

	__slots__ = ["_Ctct", "_Age", "_CstmrFileRefNb", "_Id", "_Adr", "_Nm"]
	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def Age(self):
		return self._Age

	@Age.setter
	def Age(self, value):
		self._Age = value if type(value) != auto else self.make_default("Age")

	@Age.deleter
	def Age(self):
		del self._Age
		self._Age = None

	@property
	def CstmrFileRefNb(self):
		return self._CstmrFileRefNb

	@CstmrFileRefNb.setter
	def CstmrFileRefNb(self, value):
		self._CstmrFileRefNb = value if type(value) != auto else self.make_default("CstmrFileRefNb")

	@CstmrFileRefNb.deleter
	def CstmrFileRefNb(self):
		del self._CstmrFileRefNb
		self._CstmrFileRefNb = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Age', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrFileRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Credentials3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

