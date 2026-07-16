# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class ResponseType8(base_types._BaseFieldType):

	__slots__ = ["_AddtlRspnInf", "_Cdfctn", "_Rspn", "_RspnRsn", "_RspndrId"]
	@property
	def AddtlRspnInf(self):
		return self._AddtlRspnInf

	@AddtlRspnInf.setter
	def AddtlRspnInf(self, value):
		self._AddtlRspnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRspnInf', Max35Text, False)

	@AddtlRspnInf.deleter
	def AddtlRspnInf(self):
		del self._AddtlRspnInf
		self._AddtlRspnInf = base_types.UninitialisedField(self, 'AddtlRspnInf', Max35Text, False)

	@property
	def Cdfctn(self):
		return self._Cdfctn

	@Cdfctn.setter
	def Cdfctn(self, value):
		self._Cdfctn = value if value is not None else base_types.UninitialisedField(self, 'Cdfctn', Max35Text, False)

	@Cdfctn.deleter
	def Cdfctn(self):
		del self._Cdfctn
		self._Cdfctn = base_types.UninitialisedField(self, 'Cdfctn', Max35Text, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', Max35Text, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', Max35Text, False)

	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if value is not None else base_types.UninitialisedField(self, 'RspnRsn', Max35Text, False)

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = base_types.UninitialisedField(self, 'RspnRsn', Max35Text, False)

	@property
	def RspndrId(self):
		return self._RspndrId

	@RspndrId.setter
	def RspndrId(self, value):
		self._RspndrId = value if value is not None else base_types.UninitialisedField(self, 'RspndrId', Max35Text, False)

	@RspndrId.deleter
	def RspndrId(self):
		del self._RspndrId
		self._RspndrId = base_types.UninitialisedField(self, 'RspndrId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRspnInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdfctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspndrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))