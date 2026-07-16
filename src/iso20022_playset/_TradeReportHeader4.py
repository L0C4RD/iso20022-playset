# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max100Text
from . import Number
from . import OrganisationIdentification15Choice
from . import Pagination1

class TradeReportHeader4(base_types._BaseFieldType):

	__slots__ = ["_CmptntAuthrty", "_MsgPgntn", "_NbRcrds", "_NewTradRpstryIdr", "_RptExctnDt", "_RptgPurp"]
	@property
	def CmptntAuthrty(self):
		return self._CmptntAuthrty

	@CmptntAuthrty.setter
	def CmptntAuthrty(self, value):
		self._CmptntAuthrty = value if value is not None else base_types.UninitialisedField(self, 'CmptntAuthrty', Max100Text, True)

	@CmptntAuthrty.deleter
	def CmptntAuthrty(self):
		del self._CmptntAuthrty
		self._CmptntAuthrty = base_types.UninitialisedField(self, 'CmptntAuthrty', Max100Text, True)

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@property
	def NbRcrds(self):
		return self._NbRcrds

	@NbRcrds.setter
	def NbRcrds(self, value):
		self._NbRcrds = value if value is not None else base_types.UninitialisedField(self, 'NbRcrds', Number, False)

	@NbRcrds.deleter
	def NbRcrds(self):
		del self._NbRcrds
		self._NbRcrds = base_types.UninitialisedField(self, 'NbRcrds', Number, False)

	@property
	def NewTradRpstryIdr(self):
		return self._NewTradRpstryIdr

	@NewTradRpstryIdr.setter
	def NewTradRpstryIdr(self, value):
		self._NewTradRpstryIdr = value if value is not None else base_types.UninitialisedField(self, 'NewTradRpstryIdr', OrganisationIdentification15Choice, False)

	@NewTradRpstryIdr.deleter
	def NewTradRpstryIdr(self):
		del self._NewTradRpstryIdr
		self._NewTradRpstryIdr = base_types.UninitialisedField(self, 'NewTradRpstryIdr', OrganisationIdentification15Choice, False)

	@property
	def RptExctnDt(self):
		return self._RptExctnDt

	@RptExctnDt.setter
	def RptExctnDt(self, value):
		self._RptExctnDt = value if value is not None else base_types.UninitialisedField(self, 'RptExctnDt', ISODate, False)

	@RptExctnDt.deleter
	def RptExctnDt(self):
		del self._RptExctnDt
		self._RptExctnDt = base_types.UninitialisedField(self, 'RptExctnDt', ISODate, False)

	@property
	def RptgPurp(self):
		return self._RptgPurp

	@RptgPurp.setter
	def RptgPurp(self, value):
		self._RptgPurp = value if value is not None else base_types.UninitialisedField(self, 'RptgPurp', Max100Text, True)

	@RptgPurp.deleter
	def RptgPurp(self):
		del self._RptgPurp
		self._RptgPurp = base_types.UninitialisedField(self, 'RptgPurp', Max100Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmptntAuthrty', type=Max100Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbRcrds', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewTradRpstryIdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPurp', type=Max100Text, min=0, max=None, mutex_group=None, array=True),
	))