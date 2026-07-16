# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDevice2Code
from . import ATMEquipment1
from . import ActiveCurrencyCode
from . import Max35Text
from . import MessageProtection1Code
from . import PostalAddress17
from . import TransactionEnvironment2Code

class AutomatedTellerMachine5(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_BaseCcy", "_Eqpmnt", "_Id", "_Lctn", "_LctnCtgy", "_MsgPrtcn", "_OutOfSvcDvc", "_SeqNb"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', Max35Text, False)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', Max35Text, False)

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if value is not None else base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@property
	def Eqpmnt(self):
		return self._Eqpmnt

	@Eqpmnt.setter
	def Eqpmnt(self, value):
		self._Eqpmnt = value if value is not None else base_types.UninitialisedField(self, 'Eqpmnt', ATMEquipment1, False)

	@Eqpmnt.deleter
	def Eqpmnt(self):
		del self._Eqpmnt
		self._Eqpmnt = base_types.UninitialisedField(self, 'Eqpmnt', ATMEquipment1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', PostalAddress17, False)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', PostalAddress17, False)

	@property
	def LctnCtgy(self):
		return self._LctnCtgy

	@LctnCtgy.setter
	def LctnCtgy(self, value):
		self._LctnCtgy = value if value is not None else base_types.UninitialisedField(self, 'LctnCtgy', TransactionEnvironment2Code, False)

	@LctnCtgy.deleter
	def LctnCtgy(self):
		del self._LctnCtgy
		self._LctnCtgy = base_types.UninitialisedField(self, 'LctnCtgy', TransactionEnvironment2Code, False)

	@property
	def MsgPrtcn(self):
		return self._MsgPrtcn

	@MsgPrtcn.setter
	def MsgPrtcn(self, value):
		self._MsgPrtcn = value if value is not None else base_types.UninitialisedField(self, 'MsgPrtcn', MessageProtection1Code, False)

	@MsgPrtcn.deleter
	def MsgPrtcn(self):
		del self._MsgPrtcn
		self._MsgPrtcn = base_types.UninitialisedField(self, 'MsgPrtcn', MessageProtection1Code, False)

	@property
	def OutOfSvcDvc(self):
		return self._OutOfSvcDvc

	@OutOfSvcDvc.setter
	def OutOfSvcDvc(self, value):
		self._OutOfSvcDvc = value if value is not None else base_types.UninitialisedField(self, 'OutOfSvcDvc', ATMDevice2Code, True)

	@OutOfSvcDvc.deleter
	def OutOfSvcDvc(self):
		del self._OutOfSvcDvc
		self._OutOfSvcDvc = base_types.UninitialisedField(self, 'OutOfSvcDvc', ATMDevice2Code, True)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqpmnt', type=ATMEquipment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=PostalAddress17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCtgy', type=TransactionEnvironment2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPrtcn', type=MessageProtection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutOfSvcDvc', type=ATMDevice2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))