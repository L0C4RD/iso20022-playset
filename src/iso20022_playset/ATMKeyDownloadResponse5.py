import base_types
import Max140Binary
import ATMCommand17
import ATMEnvironment7
import SecurityParameters10
import ATMSecurityContext3

class ATMKeyDownloadResponse5(base_types._BaseFieldType):

	__slots__ = ["_HstSctyParams", "_ATMChllng", "_ATMSctyCntxt", "_Cmd", "_Envt"]
	@property
	def HstSctyParams(self):
		return self._HstSctyParams

	@HstSctyParams.setter
	def HstSctyParams(self, value):
		self._HstSctyParams = value if type(value) != auto else self.make_default("HstSctyParams")

	@HstSctyParams.deleter
	def HstSctyParams(self):
		del self._HstSctyParams
		self._HstSctyParams = None

	@property
	def ATMChllng(self):
		return self._ATMChllng

	@ATMChllng.setter
	def ATMChllng(self, value):
		self._ATMChllng = value if type(value) != auto else self.make_default("ATMChllng")

	@ATMChllng.deleter
	def ATMChllng(self):
		del self._ATMChllng
		self._ATMChllng = None

	@property
	def ATMSctyCntxt(self):
		return self._ATMSctyCntxt

	@ATMSctyCntxt.setter
	def ATMSctyCntxt(self, value):
		self._ATMSctyCntxt = value if type(value) != auto else self.make_default("ATMSctyCntxt")

	@ATMSctyCntxt.deleter
	def ATMSctyCntxt(self):
		del self._ATMSctyCntxt
		self._ATMSctyCntxt = None

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstSctyParams', type=SecurityParameters10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSctyCntxt', type=ATMSecurityContext3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
	))

