# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalReference10 import AdditionalReference10
from ._CopyInformation5 import CopyInformation5
from ._Extension1 import Extension1
from ._MessageIdentification1 import MessageIdentification1
from ._RedemptionMultipleExecution6 import RedemptionMultipleExecution6

class RedemptionOrderConfirmationV05(base_types._BaseFieldType):

	__slots__ = ["_CpyDtls", "_MltplExctnDtls", "_MsgId", "_PoolRef", "_PrvsRef", "_RltdRef", "_Xtnsn"]
	@property
	def CpyDtls(self):
		return self._CpyDtls

	@CpyDtls.setter
	def CpyDtls(self, value):
		self._CpyDtls = value if type(value) != base_types.auto else self.make_default("CpyDtls")

	@CpyDtls.deleter
	def CpyDtls(self):
		del self._CpyDtls
		self._CpyDtls = None

	@property
	def MltplExctnDtls(self):
		return self._MltplExctnDtls

	@MltplExctnDtls.setter
	def MltplExctnDtls(self, value):
		self._MltplExctnDtls = value if type(value) != base_types.auto else self.make_default("MltplExctnDtls")

	@MltplExctnDtls.deleter
	def MltplExctnDtls(self):
		del self._MltplExctnDtls
		self._MltplExctnDtls = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != base_types.auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplExctnDtls', type=RedemptionMultipleExecution6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))