import base_types
import ActiveCurrencyAndAmount
import ISODate
import YesNoIndicator
import Max140Text

class DebitAuthorisationConfirmation2(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_ValDtToDbt", "_AmtToDbt", "_DbtAuthstn"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def ValDtToDbt(self):
		return self._ValDtToDbt

	@ValDtToDbt.setter
	def ValDtToDbt(self, value):
		self._ValDtToDbt = value if type(value) != auto else self.make_default("ValDtToDbt")

	@ValDtToDbt.deleter
	def ValDtToDbt(self):
		del self._ValDtToDbt
		self._ValDtToDbt = None

	@property
	def AmtToDbt(self):
		return self._AmtToDbt

	@AmtToDbt.setter
	def AmtToDbt(self, value):
		self._AmtToDbt = value if type(value) != auto else self.make_default("AmtToDbt")

	@AmtToDbt.deleter
	def AmtToDbt(self):
		del self._AmtToDbt
		self._AmtToDbt = None

	@property
	def DbtAuthstn(self):
		return self._DbtAuthstn

	@DbtAuthstn.setter
	def DbtAuthstn(self, value):
		self._DbtAuthstn = value if type(value) != auto else self.make_default("DbtAuthstn")

	@DbtAuthstn.deleter
	def DbtAuthstn(self):
		del self._DbtAuthstn
		self._DbtAuthstn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtToDbt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtToDbt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAuthstn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

