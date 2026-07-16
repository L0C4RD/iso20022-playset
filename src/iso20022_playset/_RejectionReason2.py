# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max20000Text
from . import Max350Text
from . import Max35Text

class RejectionReason2(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_ErrLctn", "_RjctgPtyRsn", "_RjctnDtTm", "_RsnDesc"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', Max20000Text, False)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', Max20000Text, False)

	@property
	def ErrLctn(self):
		return self._ErrLctn

	@ErrLctn.setter
	def ErrLctn(self, value):
		self._ErrLctn = value if value is not None else base_types.UninitialisedField(self, 'ErrLctn', Max350Text, False)

	@ErrLctn.deleter
	def ErrLctn(self):
		del self._ErrLctn
		self._ErrLctn = base_types.UninitialisedField(self, 'ErrLctn', Max350Text, False)

	@property
	def RjctgPtyRsn(self):
		return self._RjctgPtyRsn

	@RjctgPtyRsn.setter
	def RjctgPtyRsn(self, value):
		self._RjctgPtyRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctgPtyRsn', Max35Text, False)

	@RjctgPtyRsn.deleter
	def RjctgPtyRsn(self):
		del self._RjctgPtyRsn
		self._RjctgPtyRsn = base_types.UninitialisedField(self, 'RjctgPtyRsn', Max35Text, False)

	@property
	def RjctnDtTm(self):
		return self._RjctnDtTm

	@RjctnDtTm.setter
	def RjctnDtTm(self, value):
		self._RjctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'RjctnDtTm', ISODateTime, False)

	@RjctnDtTm.deleter
	def RjctnDtTm(self):
		del self._RjctnDtTm
		self._RjctnDtTm = base_types.UninitialisedField(self, 'RjctnDtTm', ISODateTime, False)

	@property
	def RsnDesc(self):
		return self._RsnDesc

	@RsnDesc.setter
	def RsnDesc(self, value):
		self._RsnDesc = value if value is not None else base_types.UninitialisedField(self, 'RsnDesc', Max350Text, False)

	@RsnDesc.deleter
	def RsnDesc(self):
		del self._RsnDesc
		self._RsnDesc = base_types.UninitialisedField(self, 'RsnDesc', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrLctn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctgPtyRsn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))