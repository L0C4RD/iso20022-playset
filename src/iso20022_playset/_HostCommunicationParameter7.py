# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CAPEEncodingMode1Code
from . import CAPEExchangeMode1Code
from . import KEKIdentifier5
from . import Max35Text
from . import NetworkParameters7
from . import PhysicalInterfaceParameter1
from . import TerminalManagementAction3Code

class HostCommunicationParameter7(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_Adr", "_HstId", "_Key", "_NcodgMd", "_NtwkSvcPrvdr", "_PhysIntrfc", "_XchgMd"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', NetworkParameters7, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', NetworkParameters7, False)

	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if value is not None else base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if value is not None else base_types.UninitialisedField(self, 'Key', KEKIdentifier5, True)

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = base_types.UninitialisedField(self, 'Key', KEKIdentifier5, True)

	@property
	def NcodgMd(self):
		return self._NcodgMd

	@NcodgMd.setter
	def NcodgMd(self, value):
		self._NcodgMd = value if value is not None else base_types.UninitialisedField(self, 'NcodgMd', CAPEEncodingMode1Code, False)

	@NcodgMd.deleter
	def NcodgMd(self):
		del self._NcodgMd
		self._NcodgMd = base_types.UninitialisedField(self, 'NcodgMd', CAPEEncodingMode1Code, False)

	@property
	def NtwkSvcPrvdr(self):
		return self._NtwkSvcPrvdr

	@NtwkSvcPrvdr.setter
	def NtwkSvcPrvdr(self, value):
		self._NtwkSvcPrvdr = value if value is not None else base_types.UninitialisedField(self, 'NtwkSvcPrvdr', NetworkParameters7, False)

	@NtwkSvcPrvdr.deleter
	def NtwkSvcPrvdr(self):
		del self._NtwkSvcPrvdr
		self._NtwkSvcPrvdr = base_types.UninitialisedField(self, 'NtwkSvcPrvdr', NetworkParameters7, False)

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
	def XchgMd(self):
		return self._XchgMd

	@XchgMd.setter
	def XchgMd(self, value):
		self._XchgMd = value if value is not None else base_types.UninitialisedField(self, 'XchgMd', CAPEExchangeMode1Code, False)

	@XchgMd.deleter
	def XchgMd(self):
		del self._XchgMd
		self._XchgMd = base_types.UninitialisedField(self, 'XchgMd', CAPEExchangeMode1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=KEKIdentifier5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NcodgMd', type=CAPEEncodingMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkSvcPrvdr', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysIntrfc', type=PhysicalInterfaceParameter1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgMd', type=CAPEExchangeMode1Code, min=0, max=1, mutex_group=None, array=False),
	))