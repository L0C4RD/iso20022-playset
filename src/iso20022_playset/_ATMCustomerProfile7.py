# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMService28
from . import Max35Text
from . import Max70Text

class ATMCustomerProfile7(base_types._BaseFieldType):

	__slots__ = ["_AllwdSvcs", "_CstmrId", "_PrflDesc", "_PrflRef"]
	@property
	def AllwdSvcs(self):
		return self._AllwdSvcs

	@AllwdSvcs.setter
	def AllwdSvcs(self, value):
		self._AllwdSvcs = value if value is not None else base_types.UninitialisedField(self, 'AllwdSvcs', ATMService28, True)

	@AllwdSvcs.deleter
	def AllwdSvcs(self):
		del self._AllwdSvcs
		self._AllwdSvcs = base_types.UninitialisedField(self, 'AllwdSvcs', ATMService28, True)

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if value is not None else base_types.UninitialisedField(self, 'CstmrId', Max35Text, False)

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = base_types.UninitialisedField(self, 'CstmrId', Max35Text, False)

	@property
	def PrflDesc(self):
		return self._PrflDesc

	@PrflDesc.setter
	def PrflDesc(self, value):
		self._PrflDesc = value if value is not None else base_types.UninitialisedField(self, 'PrflDesc', Max70Text, False)

	@PrflDesc.deleter
	def PrflDesc(self):
		del self._PrflDesc
		self._PrflDesc = base_types.UninitialisedField(self, 'PrflDesc', Max70Text, False)

	@property
	def PrflRef(self):
		return self._PrflRef

	@PrflRef.setter
	def PrflRef(self, value):
		self._PrflRef = value if value is not None else base_types.UninitialisedField(self, 'PrflRef', Max35Text, False)

	@PrflRef.deleter
	def PrflRef(self):
		del self._PrflRef
		self._PrflRef = base_types.UninitialisedField(self, 'PrflRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllwdSvcs', type=ATMService28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))