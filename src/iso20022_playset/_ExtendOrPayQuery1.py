# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankInstructions1
from . import Contacts3
from . import Demand2
from . import Document9
from . import ISODate
from . import Max2000Text
from . import Undertaking9

class ExtendOrPayQuery1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_BkCtct", "_BkInstrs", "_DmndDtls", "_NclsdFile", "_ReqdXpryDt", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def BkCtct(self):
		return self._BkCtct

	@BkCtct.setter
	def BkCtct(self, value):
		self._BkCtct = value if value is not None else base_types.UninitialisedField(self, 'BkCtct', Contacts3, True)

	@BkCtct.deleter
	def BkCtct(self):
		del self._BkCtct
		self._BkCtct = base_types.UninitialisedField(self, 'BkCtct', Contacts3, True)

	@property
	def BkInstrs(self):
		return self._BkInstrs

	@BkInstrs.setter
	def BkInstrs(self, value):
		self._BkInstrs = value if value is not None else base_types.UninitialisedField(self, 'BkInstrs', BankInstructions1, False)

	@BkInstrs.deleter
	def BkInstrs(self):
		del self._BkInstrs
		self._BkInstrs = base_types.UninitialisedField(self, 'BkInstrs', BankInstructions1, False)

	@property
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if value is not None else base_types.UninitialisedField(self, 'DmndDtls', Demand2, False)

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = base_types.UninitialisedField(self, 'DmndDtls', Demand2, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@property
	def ReqdXpryDt(self):
		return self._ReqdXpryDt

	@ReqdXpryDt.setter
	def ReqdXpryDt(self, value):
		self._ReqdXpryDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdXpryDt', ISODate, False)

	@ReqdXpryDt.deleter
	def ReqdXpryDt(self):
		del self._ReqdXpryDt
		self._ReqdXpryDt = base_types.UninitialisedField(self, 'ReqdXpryDt', ISODate, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkCtct', type=Contacts3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkInstrs', type=BankInstructions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDtls', type=Demand2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdXpryDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))