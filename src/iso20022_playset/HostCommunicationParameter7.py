import base_types
import TerminalManagementAction3Code
import NetworkParameters7
import Max35Text
import KEKIdentifier5
import PhysicalInterfaceParameter1
import CAPEEncodingMode1Code
import CAPEExchangeMode1Code

class HostCommunicationParameter7(base_types._BaseFieldType):

	__slots__ = ["_NcodgMd", "_XchgMd", "_PhysIntrfc", "_ActnTp", "_HstId", "_Adr", "_NtwkSvcPrvdr", "_Key"]
	@property
	def NcodgMd(self):
		return self._NcodgMd

	@NcodgMd.setter
	def NcodgMd(self, value):
		self._NcodgMd = value if type(value) != auto else self.make_default("NcodgMd")

	@NcodgMd.deleter
	def NcodgMd(self):
		del self._NcodgMd
		self._NcodgMd = None

	@property
	def XchgMd(self):
		return self._XchgMd

	@XchgMd.setter
	def XchgMd(self, value):
		self._XchgMd = value if type(value) != auto else self.make_default("XchgMd")

	@XchgMd.deleter
	def XchgMd(self):
		del self._XchgMd
		self._XchgMd = None

	@property
	def PhysIntrfc(self):
		return self._PhysIntrfc

	@PhysIntrfc.setter
	def PhysIntrfc(self, value):
		self._PhysIntrfc = value if type(value) != auto else self.make_default("PhysIntrfc")

	@PhysIntrfc.deleter
	def PhysIntrfc(self):
		del self._PhysIntrfc
		self._PhysIntrfc = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if type(value) != auto else self.make_default("HstId")

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = None

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
	def NtwkSvcPrvdr(self):
		return self._NtwkSvcPrvdr

	@NtwkSvcPrvdr.setter
	def NtwkSvcPrvdr(self, value):
		self._NtwkSvcPrvdr = value if type(value) != auto else self.make_default("NtwkSvcPrvdr")

	@NtwkSvcPrvdr.deleter
	def NtwkSvcPrvdr(self):
		del self._NtwkSvcPrvdr
		self._NtwkSvcPrvdr = None

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NcodgMd', type=CAPEEncodingMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgMd', type=CAPEExchangeMode1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysIntrfc', type=PhysicalInterfaceParameter1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkSvcPrvdr', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=KEKIdentifier5, min=0, max=None, mutex_group=None, array=True),
	))

