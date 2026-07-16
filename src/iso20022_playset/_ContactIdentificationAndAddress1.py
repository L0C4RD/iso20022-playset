# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress8
from . import Max35Text
from . import PaymentRole1Code

class ContactIdentificationAndAddress1(base_types._BaseFieldType):

	__slots__ = ["_ComAdr", "_Nm", "_Role"]
	@property
	def ComAdr(self):
		return self._ComAdr

	@ComAdr.setter
	def ComAdr(self, value):
		self._ComAdr = value if value is not None else base_types.UninitialisedField(self, 'ComAdr', CommunicationAddress8, False)

	@ComAdr.deleter
	def ComAdr(self):
		del self._ComAdr
		self._ComAdr = base_types.UninitialisedField(self, 'ComAdr', CommunicationAddress8, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', PaymentRole1Code, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', PaymentRole1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComAdr', type=CommunicationAddress8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PaymentRole1Code, min=1, max=1, mutex_group=None, array=False),
	))