# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage11
from . import DocumentType7Code
from . import TrueFalseIndicator

class PaymentReceipt6(base_types._BaseFieldType):

	__slots__ = ["_DocQlfr", "_IntgrtdPrtFlg", "_OutptCntt", "_ReqrdSgntrFlg"]
	@property
	def DocQlfr(self):
		return self._DocQlfr

	@DocQlfr.setter
	def DocQlfr(self, value):
		self._DocQlfr = value if value is not None else base_types.UninitialisedField(self, 'DocQlfr', DocumentType7Code, False)

	@DocQlfr.deleter
	def DocQlfr(self):
		del self._DocQlfr
		self._DocQlfr = base_types.UninitialisedField(self, 'DocQlfr', DocumentType7Code, False)

	@property
	def IntgrtdPrtFlg(self):
		return self._IntgrtdPrtFlg

	@IntgrtdPrtFlg.setter
	def IntgrtdPrtFlg(self, value):
		self._IntgrtdPrtFlg = value if value is not None else base_types.UninitialisedField(self, 'IntgrtdPrtFlg', TrueFalseIndicator, False)

	@IntgrtdPrtFlg.deleter
	def IntgrtdPrtFlg(self):
		del self._IntgrtdPrtFlg
		self._IntgrtdPrtFlg = base_types.UninitialisedField(self, 'IntgrtdPrtFlg', TrueFalseIndicator, False)

	@property
	def OutptCntt(self):
		return self._OutptCntt

	@OutptCntt.setter
	def OutptCntt(self, value):
		self._OutptCntt = value if value is not None else base_types.UninitialisedField(self, 'OutptCntt', ActionMessage11, False)

	@OutptCntt.deleter
	def OutptCntt(self):
		del self._OutptCntt
		self._OutptCntt = base_types.UninitialisedField(self, 'OutptCntt', ActionMessage11, False)

	@property
	def ReqrdSgntrFlg(self):
		return self._ReqrdSgntrFlg

	@ReqrdSgntrFlg.setter
	def ReqrdSgntrFlg(self, value):
		self._ReqrdSgntrFlg = value if value is not None else base_types.UninitialisedField(self, 'ReqrdSgntrFlg', TrueFalseIndicator, False)

	@ReqrdSgntrFlg.deleter
	def ReqrdSgntrFlg(self):
		del self._ReqrdSgntrFlg
		self._ReqrdSgntrFlg = base_types.UninitialisedField(self, 'ReqrdSgntrFlg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocQlfr', type=DocumentType7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntgrtdPrtFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptCntt', type=ActionMessage11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdSgntrFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))