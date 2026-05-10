import base_types
import DocumentType7Code
import ActionMessage11
import TrueFalseIndicator

class PaymentReceipt6(base_types._BaseFieldType):

	__slots__ = ["_DocQlfr", "_OutptCntt", "_IntgrtdPrtFlg", "_ReqrdSgntrFlg"]
	@property
	def DocQlfr(self):
		return self._DocQlfr

	@DocQlfr.setter
	def DocQlfr(self, value):
		self._DocQlfr = value if type(value) != auto else self.make_default("DocQlfr")

	@DocQlfr.deleter
	def DocQlfr(self):
		del self._DocQlfr
		self._DocQlfr = None

	@property
	def OutptCntt(self):
		return self._OutptCntt

	@OutptCntt.setter
	def OutptCntt(self, value):
		self._OutptCntt = value if type(value) != auto else self.make_default("OutptCntt")

	@OutptCntt.deleter
	def OutptCntt(self):
		del self._OutptCntt
		self._OutptCntt = None

	@property
	def IntgrtdPrtFlg(self):
		return self._IntgrtdPrtFlg

	@IntgrtdPrtFlg.setter
	def IntgrtdPrtFlg(self, value):
		self._IntgrtdPrtFlg = value if type(value) != auto else self.make_default("IntgrtdPrtFlg")

	@IntgrtdPrtFlg.deleter
	def IntgrtdPrtFlg(self):
		del self._IntgrtdPrtFlg
		self._IntgrtdPrtFlg = None

	@property
	def ReqrdSgntrFlg(self):
		return self._ReqrdSgntrFlg

	@ReqrdSgntrFlg.setter
	def ReqrdSgntrFlg(self, value):
		self._ReqrdSgntrFlg = value if type(value) != auto else self.make_default("ReqrdSgntrFlg")

	@ReqrdSgntrFlg.deleter
	def ReqrdSgntrFlg(self):
		del self._ReqrdSgntrFlg
		self._ReqrdSgntrFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocQlfr', type=DocumentType7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptCntt', type=ActionMessage11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntgrtdPrtFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdSgntrFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

