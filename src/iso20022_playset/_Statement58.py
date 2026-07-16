# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TrueFalseIndicator
from . import YesNoIndicator

class Statement58(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_HstrcData", "_QryRef", "_RptId", "_SubAcctInd"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@property
	def HstrcData(self):
		return self._HstrcData

	@HstrcData.setter
	def HstrcData(self, value):
		self._HstrcData = value if value is not None else base_types.UninitialisedField(self, 'HstrcData', TrueFalseIndicator, False)

	@HstrcData.deleter
	def HstrcData(self):
		del self._HstrcData
		self._HstrcData = base_types.UninitialisedField(self, 'HstrcData', TrueFalseIndicator, False)

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@property
	def SubAcctInd(self):
		return self._SubAcctInd

	@SubAcctInd.setter
	def SubAcctInd(self, value):
		self._SubAcctInd = value if value is not None else base_types.UninitialisedField(self, 'SubAcctInd', YesNoIndicator, False)

	@SubAcctInd.deleter
	def SubAcctInd(self):
		del self._SubAcctInd
		self._SubAcctInd = base_types.UninitialisedField(self, 'SubAcctInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstrcData', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))