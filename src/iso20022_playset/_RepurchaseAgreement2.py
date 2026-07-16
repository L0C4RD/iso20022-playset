# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODate
from . import LEIIdentifier
from . import RepurchaseAgreementType3Choice

class RepurchaseAgreement2(base_types._BaseFieldType):

	__slots__ = ["_CollMktVal", "_CtrPty", "_MtrtyDt", "_RpAgrmtTp", "_ScndLegPric", "_TrptyAgtId"]
	@property
	def CollMktVal(self):
		return self._CollMktVal

	@CollMktVal.setter
	def CollMktVal(self, value):
		self._CollMktVal = value if value is not None else base_types.UninitialisedField(self, 'CollMktVal', ActiveCurrencyAndAmount, False)

	@CollMktVal.deleter
	def CollMktVal(self):
		del self._CollMktVal
		self._CollMktVal = base_types.UninitialisedField(self, 'CollMktVal', ActiveCurrencyAndAmount, False)

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', LEIIdentifier, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', LEIIdentifier, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def RpAgrmtTp(self):
		return self._RpAgrmtTp

	@RpAgrmtTp.setter
	def RpAgrmtTp(self, value):
		self._RpAgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'RpAgrmtTp', RepurchaseAgreementType3Choice, False)

	@RpAgrmtTp.deleter
	def RpAgrmtTp(self):
		del self._RpAgrmtTp
		self._RpAgrmtTp = base_types.UninitialisedField(self, 'RpAgrmtTp', RepurchaseAgreementType3Choice, False)

	@property
	def ScndLegPric(self):
		return self._ScndLegPric

	@ScndLegPric.setter
	def ScndLegPric(self, value):
		self._ScndLegPric = value if value is not None else base_types.UninitialisedField(self, 'ScndLegPric', ActiveCurrencyAndAmount, False)

	@ScndLegPric.deleter
	def ScndLegPric(self):
		del self._ScndLegPric
		self._ScndLegPric = base_types.UninitialisedField(self, 'ScndLegPric', ActiveCurrencyAndAmount, False)

	@property
	def TrptyAgtId(self):
		return self._TrptyAgtId

	@TrptyAgtId.setter
	def TrptyAgtId(self, value):
		self._TrptyAgtId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtId', LEIIdentifier, False)

	@TrptyAgtId.deleter
	def TrptyAgtId(self):
		del self._TrptyAgtId
		self._TrptyAgtId = base_types.UninitialisedField(self, 'TrptyAgtId', LEIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMktVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmtTp', type=RepurchaseAgreementType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLegPric', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))