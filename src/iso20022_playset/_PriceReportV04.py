# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference3
from . import Extension1
from . import Max35Text
from . import MessageIdentification1
from . import Pagination
from . import PriceReportFunction1Code
from . import PriceValuation4

class PriceReportV04(base_types._BaseFieldType):

	__slots__ = ["_CxlId", "_Fctn", "_MsgId", "_MsgPgntn", "_PoolRef", "_PricRptId", "_PricValtnDtls", "_PrvsRef", "_RltdRef", "_Xtnsn"]
	@property
	def CxlId(self):
		return self._CxlId

	@CxlId.setter
	def CxlId(self, value):
		self._CxlId = value if value is not None else base_types.UninitialisedField(self, 'CxlId', Max35Text, False)

	@CxlId.deleter
	def CxlId(self):
		del self._CxlId
		self._CxlId = base_types.UninitialisedField(self, 'CxlId', Max35Text, False)

	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if value is not None else base_types.UninitialisedField(self, 'Fctn', PriceReportFunction1Code, False)

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = base_types.UninitialisedField(self, 'Fctn', PriceReportFunction1Code, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination, False)

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if value is not None else base_types.UninitialisedField(self, 'PoolRef', AdditionalReference3, False)

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = base_types.UninitialisedField(self, 'PoolRef', AdditionalReference3, False)

	@property
	def PricRptId(self):
		return self._PricRptId

	@PricRptId.setter
	def PricRptId(self, value):
		self._PricRptId = value if value is not None else base_types.UninitialisedField(self, 'PricRptId', Max35Text, False)

	@PricRptId.deleter
	def PricRptId(self):
		del self._PricRptId
		self._PricRptId = base_types.UninitialisedField(self, 'PricRptId', Max35Text, False)

	@property
	def PricValtnDtls(self):
		return self._PricValtnDtls

	@PricValtnDtls.setter
	def PricValtnDtls(self, value):
		self._PricValtnDtls = value if value is not None else base_types.UninitialisedField(self, 'PricValtnDtls', PriceValuation4, True)

	@PricValtnDtls.deleter
	def PricValtnDtls(self):
		del self._PricValtnDtls
		self._PricValtnDtls = base_types.UninitialisedField(self, 'PricValtnDtls', PriceValuation4, True)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference3, True)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference3, True)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference3, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference3, False)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=PriceReportFunction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricValtnDtls', type=PriceValuation4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))