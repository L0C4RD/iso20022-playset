# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max10NumericText
from . import UnitOfMeasure10Code

class Distance1(base_types._BaseFieldType):

	__slots__ = ["_FreeDstnc", "_OdmtrRtr", "_OdmtrStart", "_Rate", "_TtlDstnc", "_UnitOfMeasr"]
	@property
	def FreeDstnc(self):
		return self._FreeDstnc

	@FreeDstnc.setter
	def FreeDstnc(self, value):
		self._FreeDstnc = value if value is not None else base_types.UninitialisedField(self, 'FreeDstnc', Max10NumericText, False)

	@FreeDstnc.deleter
	def FreeDstnc(self):
		del self._FreeDstnc
		self._FreeDstnc = base_types.UninitialisedField(self, 'FreeDstnc', Max10NumericText, False)

	@property
	def OdmtrRtr(self):
		return self._OdmtrRtr

	@OdmtrRtr.setter
	def OdmtrRtr(self, value):
		self._OdmtrRtr = value if value is not None else base_types.UninitialisedField(self, 'OdmtrRtr', Max10NumericText, False)

	@OdmtrRtr.deleter
	def OdmtrRtr(self):
		del self._OdmtrRtr
		self._OdmtrRtr = base_types.UninitialisedField(self, 'OdmtrRtr', Max10NumericText, False)

	@property
	def OdmtrStart(self):
		return self._OdmtrStart

	@OdmtrStart.setter
	def OdmtrStart(self, value):
		self._OdmtrStart = value if value is not None else base_types.UninitialisedField(self, 'OdmtrStart', Max10NumericText, False)

	@OdmtrStart.deleter
	def OdmtrStart(self):
		del self._OdmtrStart
		self._OdmtrStart = base_types.UninitialisedField(self, 'OdmtrStart', Max10NumericText, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', ImpliedCurrencyAndAmount, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', ImpliedCurrencyAndAmount, False)

	@property
	def TtlDstnc(self):
		return self._TtlDstnc

	@TtlDstnc.setter
	def TtlDstnc(self, value):
		self._TtlDstnc = value if value is not None else base_types.UninitialisedField(self, 'TtlDstnc', Max10NumericText, False)

	@TtlDstnc.deleter
	def TtlDstnc(self):
		del self._TtlDstnc
		self._TtlDstnc = base_types.UninitialisedField(self, 'TtlDstnc', Max10NumericText, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure10Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure10Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FreeDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrRtr', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrStart', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure10Code, min=0, max=1, mutex_group=None, array=False),
	))