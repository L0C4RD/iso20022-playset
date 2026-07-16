# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCustomerProfile1Code
from . import LanguageCode
from . import Max35Text

class ATMCustomerProfile6(base_types._BaseFieldType):

	__slots__ = ["_CstmrId", "_PrefrdLang", "_PrflRef", "_RtrvlMd"]
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
	def PrefrdLang(self):
		return self._PrefrdLang

	@PrefrdLang.setter
	def PrefrdLang(self, value):
		self._PrefrdLang = value if value is not None else base_types.UninitialisedField(self, 'PrefrdLang', LanguageCode, False)

	@PrefrdLang.deleter
	def PrefrdLang(self):
		del self._PrefrdLang
		self._PrefrdLang = base_types.UninitialisedField(self, 'PrefrdLang', LanguageCode, False)

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

	@property
	def RtrvlMd(self):
		return self._RtrvlMd

	@RtrvlMd.setter
	def RtrvlMd(self, value):
		self._RtrvlMd = value if value is not None else base_types.UninitialisedField(self, 'RtrvlMd', ATMCustomerProfile1Code, False)

	@RtrvlMd.deleter
	def RtrvlMd(self):
		del self._RtrvlMd
		self._RtrvlMd = base_types.UninitialisedField(self, 'RtrvlMd', ATMCustomerProfile1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrefrdLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlMd', type=ATMCustomerProfile1Code, min=1, max=1, mutex_group=None, array=False),
	))