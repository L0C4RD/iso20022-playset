# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import ContactPersonal1
from . import Credentials3
from . import Max2NumericText
from . import Max70Text

class Customer9(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Age", "_CstmrFileRefNb", "_Ctct", "_Id", "_Nm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address2, False)

	@property
	def Age(self):
		return self._Age

	@Age.setter
	def Age(self, value):
		self._Age = value if value is not None else base_types.UninitialisedField(self, 'Age', Max2NumericText, False)

	@Age.deleter
	def Age(self):
		del self._Age
		self._Age = base_types.UninitialisedField(self, 'Age', Max2NumericText, False)

	@property
	def CstmrFileRefNb(self):
		return self._CstmrFileRefNb

	@CstmrFileRefNb.setter
	def CstmrFileRefNb(self, value):
		self._CstmrFileRefNb = value if value is not None else base_types.UninitialisedField(self, 'CstmrFileRefNb', Max70Text, False)

	@CstmrFileRefNb.deleter
	def CstmrFileRefNb(self):
		del self._CstmrFileRefNb
		self._CstmrFileRefNb = base_types.UninitialisedField(self, 'CstmrFileRefNb', Max70Text, False)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactPersonal1, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactPersonal1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Credentials3, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Credentials3, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Age', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrFileRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Credentials3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))