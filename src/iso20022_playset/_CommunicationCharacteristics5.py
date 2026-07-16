# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NetworkParameters7
from . import POICommunicationType2Code
from . import PartyType7Code
from . import PhysicalInterfaceParameter1
from . import TrueFalseIndicator

class CommunicationCharacteristics5(base_types._BaseFieldType):

	__slots__ = ["_Actv", "_ComTp", "_Params", "_PhysIntrfc", "_RmotPty"]
	@property
	def Actv(self):
		return self._Actv

	@Actv.setter
	def Actv(self, value):
		self._Actv = value if value is not None else base_types.UninitialisedField(self, 'Actv', TrueFalseIndicator, False)

	@Actv.deleter
	def Actv(self):
		del self._Actv
		self._Actv = base_types.UninitialisedField(self, 'Actv', TrueFalseIndicator, False)

	@property
	def ComTp(self):
		return self._ComTp

	@ComTp.setter
	def ComTp(self, value):
		self._ComTp = value if value is not None else base_types.UninitialisedField(self, 'ComTp', POICommunicationType2Code, False)

	@ComTp.deleter
	def ComTp(self):
		del self._ComTp
		self._ComTp = base_types.UninitialisedField(self, 'ComTp', POICommunicationType2Code, False)

	@property
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if value is not None else base_types.UninitialisedField(self, 'Params', NetworkParameters7, False)

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = base_types.UninitialisedField(self, 'Params', NetworkParameters7, False)

	@property
	def PhysIntrfc(self):
		return self._PhysIntrfc

	@PhysIntrfc.setter
	def PhysIntrfc(self, value):
		self._PhysIntrfc = value if value is not None else base_types.UninitialisedField(self, 'PhysIntrfc', PhysicalInterfaceParameter1, False)

	@PhysIntrfc.deleter
	def PhysIntrfc(self):
		del self._PhysIntrfc
		self._PhysIntrfc = base_types.UninitialisedField(self, 'PhysIntrfc', PhysicalInterfaceParameter1, False)

	@property
	def RmotPty(self):
		return self._RmotPty

	@RmotPty.setter
	def RmotPty(self, value):
		self._RmotPty = value if value is not None else base_types.UninitialisedField(self, 'RmotPty', PartyType7Code, True)

	@RmotPty.deleter
	def RmotPty(self):
		del self._RmotPty
		self._RmotPty = base_types.UninitialisedField(self, 'RmotPty', PartyType7Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actv', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComTp', type=POICommunicationType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysIntrfc', type=PhysicalInterfaceParameter1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotPty', type=PartyType7Code, min=1, max=None, mutex_group=None, array=True),
	))