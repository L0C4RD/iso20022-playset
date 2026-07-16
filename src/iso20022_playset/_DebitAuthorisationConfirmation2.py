# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODate
from . import Max140Text
from . import YesNoIndicator

class DebitAuthorisationConfirmation2(base_types._BaseFieldType):

	__slots__ = ["_AmtToDbt", "_DbtAuthstn", "_Rsn", "_ValDtToDbt"]
	@property
	def AmtToDbt(self):
		return self._AmtToDbt

	@AmtToDbt.setter
	def AmtToDbt(self, value):
		self._AmtToDbt = value if value is not None else base_types.UninitialisedField(self, 'AmtToDbt', ActiveCurrencyAndAmount, False)

	@AmtToDbt.deleter
	def AmtToDbt(self):
		del self._AmtToDbt
		self._AmtToDbt = base_types.UninitialisedField(self, 'AmtToDbt', ActiveCurrencyAndAmount, False)

	@property
	def DbtAuthstn(self):
		return self._DbtAuthstn

	@DbtAuthstn.setter
	def DbtAuthstn(self, value):
		self._DbtAuthstn = value if value is not None else base_types.UninitialisedField(self, 'DbtAuthstn', YesNoIndicator, False)

	@DbtAuthstn.deleter
	def DbtAuthstn(self):
		del self._DbtAuthstn
		self._DbtAuthstn = base_types.UninitialisedField(self, 'DbtAuthstn', YesNoIndicator, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	@property
	def ValDtToDbt(self):
		return self._ValDtToDbt

	@ValDtToDbt.setter
	def ValDtToDbt(self, value):
		self._ValDtToDbt = value if value is not None else base_types.UninitialisedField(self, 'ValDtToDbt', ISODate, False)

	@ValDtToDbt.deleter
	def ValDtToDbt(self):
		del self._ValDtToDbt
		self._ValDtToDbt = base_types.UninitialisedField(self, 'ValDtToDbt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToDbt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAuthstn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtToDbt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))