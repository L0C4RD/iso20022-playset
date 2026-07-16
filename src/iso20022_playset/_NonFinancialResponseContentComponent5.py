# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Acquirer10
from . import Action17
from . import ExternallyDefinedData5
from . import NonFinancialRequestType2Code
from . import NonFinancialResponseRisk1Code
from . import RecurringTransaction6
from . import ResponseType11

class NonFinancialResponseContentComponent5(base_types._BaseFieldType):

	__slots__ = ["_AcqrrSelctd", "_Actn", "_AddtlRspn", "_Instlmt", "_NonFinReqTp", "_RskMgmtRslt", "_Rspn"]
	@property
	def AcqrrSelctd(self):
		return self._AcqrrSelctd

	@AcqrrSelctd.setter
	def AcqrrSelctd(self, value):
		self._AcqrrSelctd = value if value is not None else base_types.UninitialisedField(self, 'AcqrrSelctd', Acquirer10, False)

	@AcqrrSelctd.deleter
	def AcqrrSelctd(self):
		del self._AcqrrSelctd
		self._AcqrrSelctd = base_types.UninitialisedField(self, 'AcqrrSelctd', Acquirer10, False)

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', Action17, True)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', Action17, True)

	@property
	def AddtlRspn(self):
		return self._AddtlRspn

	@AddtlRspn.setter
	def AddtlRspn(self, value):
		self._AddtlRspn = value if value is not None else base_types.UninitialisedField(self, 'AddtlRspn', ExternallyDefinedData5, True)

	@AddtlRspn.deleter
	def AddtlRspn(self):
		del self._AddtlRspn
		self._AddtlRspn = base_types.UninitialisedField(self, 'AddtlRspn', ExternallyDefinedData5, True)

	@property
	def Instlmt(self):
		return self._Instlmt

	@Instlmt.setter
	def Instlmt(self, value):
		self._Instlmt = value if value is not None else base_types.UninitialisedField(self, 'Instlmt', RecurringTransaction6, True)

	@Instlmt.deleter
	def Instlmt(self):
		del self._Instlmt
		self._Instlmt = base_types.UninitialisedField(self, 'Instlmt', RecurringTransaction6, True)

	@property
	def NonFinReqTp(self):
		return self._NonFinReqTp

	@NonFinReqTp.setter
	def NonFinReqTp(self, value):
		self._NonFinReqTp = value if value is not None else base_types.UninitialisedField(self, 'NonFinReqTp', NonFinancialRequestType2Code, False)

	@NonFinReqTp.deleter
	def NonFinReqTp(self):
		del self._NonFinReqTp
		self._NonFinReqTp = base_types.UninitialisedField(self, 'NonFinReqTp', NonFinancialRequestType2Code, False)

	@property
	def RskMgmtRslt(self):
		return self._RskMgmtRslt

	@RskMgmtRslt.setter
	def RskMgmtRslt(self, value):
		self._RskMgmtRslt = value if value is not None else base_types.UninitialisedField(self, 'RskMgmtRslt', NonFinancialResponseRisk1Code, False)

	@RskMgmtRslt.deleter
	def RskMgmtRslt(self):
		del self._RskMgmtRslt
		self._RskMgmtRslt = base_types.UninitialisedField(self, 'RskMgmtRslt', NonFinancialResponseRisk1Code, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrSelctd', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=Action17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlRspn', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instlmt', type=RecurringTransaction6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonFinReqTp', type=NonFinancialRequestType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskMgmtRslt', type=NonFinancialResponseRisk1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
	))